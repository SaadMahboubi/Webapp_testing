from json import load
import pytest
from server import app, loadClubs, loadCompetitions, purchasePlaces, index

@pytest.fixture
def client():
    app.config['TEST'] = True
    with app.test_client() as client:
        yield client

def test_root_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'<input' in response.data

def test_root_score(client):
    response = client.get('/score')
    assert response.status_code == 200

def test_InSummary(client):
    response = client.post("/showSummary", data = dict(email = "john@simplylift.co"),follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    print(data)
    assert "Welcome, john@simplylift.co" in data

def test_noInSummary(client):
    response = client.post("/showSummary", data = dict(email = "john@exemple.com"),follow_redirects=True)
    assert response.status_code == 403
    data = response.data.decode()
    print(data)
    assert "Désolé, cet email n&#39;a pas été trouvé" in data

def test_Booking(client):
    response = client.post("/showSummary", data = dict(email = "john@simplylift.co"),follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    print(data)
    assert "/book/Spring%20Festival/Simply%20Lift" in data

def test_invalideBooking(client):
    response = client.get("/book/Winter%20Festival/Simply%20Lift",follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    print(data)

#Achat de places ok
def test_valid_purchase_point(client):
    rv = client.post('/showSummary', data={"email":"admin@irontemple.com"}, follow_redirects=True)
    assert rv.status_code==200
    rv_test= client.get('/book/Spring%20Festival/She%20Lifts',follow_redirects=True)
    assert rv_test.status_code==200
    rv_test=client.post('/purchasePlaces', data =dict(club = 'Iron Temple', competition='Spring Festival', places = 1), follow_redirects = True)
    data =rv_test.data.decode()
    print(data)
    assert 'Number of Places: 24' in data
    assert 'Great-booking complete!' in data
    assert 'Points available: 1' in data

#Achat de places impossible car date limite dépassé
def test_inValid_purchase_point_limite_date(client):
    rv_test=client.get('/book/Fall%20Classic/Iron%20Temple')
    assert rv_test.status_code==403
    data =rv_test.data.decode()
    print(data)
    assert 'Date limite d&#39;achat dépassé, cliquez ici pour revenir en arrière :' in data

#Achat de places impossible
def test_inValid_purchase_point_more_than_12(client):
    rv_test=client.post('/purchasePlaces', data =dict(club = 'Iron Temple', competition='Spring Festival', places = 13), follow_redirects = True)
    data =rv_test.data.decode()
    print(data)
    assert 'Impossible to buy more than 12 places and less than 1' in data
    
#Achat de places impossible
def test_inValid_purchase_point_not_enought_points(client):
    rv_test=client.post('/purchasePlaces', data =dict(club = 'Iron Temple', competition='Spring Festival', places = 3), follow_redirects = True)
    data =rv_test.data.decode()
    print(data)
    assert 'Not enoought point for buy' in data
    
#Test logout
def test_logout_user(client):
    rv = client.get("/logout", follow_redirects=True)
    assert rv.status_code == 200
    data = rv.data.decode()
    print(data)
    assert "Welcome to the GUDLFT Registration Portal!" in data

def test_integration(client):
    clubs = loadClubs()
    competitions = loadCompetitions()
    response = client.get('/')
    assert response.status_code == 200
    rv_showSumm = client.post('/showSummary', data={"email":"john@simplylift.co"}, follow_redirects=True)
    assert rv_showSumm.status_code==200
    data = rv_showSumm.data.decode()
    print(data)
    assert competitions[0]['name'] in data
    assert clubs[0]['email'] in data
    
    rv_book = client.get('/book/Spring%20Festival/She%20Lifts',follow_redirects=True)
    assert rv_book.status_code==200

    rv_purchasePlaces = client.post('/purchasePlaces', data =dict(club = 'Simply Lift', competition='Spring Festival', places = 2), follow_redirects = True)
    assert rv_purchasePlaces.status_code==200
    data =rv_purchasePlaces.data.decode()
    assert 'Number of Places: 22' in data
    assert 'Points available: 7' in data
    assert 'Great-booking complete!' in data

    rv_logout = client.get("/logout", follow_redirects=True)
    assert rv_logout.status_code == 200
    data = rv_logout.data.decode()
    print(data)
    assert "Welcome to the GUDLFT Registration Portal!" in data

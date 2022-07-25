import main
import pytest
import pandas as pd
import time

g = main.Guvi()

# test for login to zen portal
@pytest.mark.first
def test_login():
    g.login()
    time.sleep(5)
    assert g.driver.current_url == "https://www.zenclass.in/class"

# test for information getting in left ribbon
@pytest.mark.second
def test_main_menu():
    """ access items from the menubar"""
    l_menu = main.g.driver.execute_script(
        " l_menu_items=document.getElementsByClassName"
        '("list-scroll py-3 color-area");'
        " l_menu_logo= document.getElementsByClassName"
        '("ml-3 d-inline-block mt-3 font-weight-bold")[0].innerText;'
        "l_menu_head=document.getElementsByClassName"
        '("list-scroll py-3 active-area active-left-bar")[0].innerText;'
        " l_menu=[];"
        """for (let index = 0; index < l_menu_items.length; index++)
               {
               l_menu[index]=l_menu_items.item(index).innerText;
               }
               l_menu.splice(0,0,l_menu_logo,l_menu_head);
               return l_menu ;"""
    )
    time.sleep(5)
    df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])
    # check dataframes
    pd.testing.assert_frame_equal(main.g.main_menu(), df_fm)
    time.sleep(5)

# test for raise a query in zen portal
@pytest.mark.thrid
def test_createquery():
  g.query()
  g.query()
  g.query()
  g.query()
  g.query()
  assert g.query() == g.query()
   


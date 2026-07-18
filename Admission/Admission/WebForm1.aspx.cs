using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Admission
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void DDSTATE_SelectedIndexChanged(object sender, EventArgs e)
        {
            if(DDSTATE.SelectedItem.Text=="Maharashtra")
            {
                DDCITY.Items.Clear();
                DDCITY.Items.Add("Kalyan");
                DDCITY.Items.Add("Thane");
            }

            if (DDSTATE.SelectedItem.Text == "Tamilnadu")
            {
                DDCITY.Items.Clear();
                DDCITY.Items.Add("Chennai");
                DDCITY.Items.Add("Coimbatore");
            }

            if (DDSTATE.SelectedItem.Text == "Kashmir")
            {
                DDCITY.Items.Clear();
                DDCITY.Items.Add("Srinagar");
                DDCITY.Items.Add("Gulmarg");
            }

        }

        protected void Langcheckbox_Click(object sender, EventArgs e)
        {
            string str = "";
                for (int i = 0; i < Language.Items.Count; i++)
            {
                if (Language.Items[i].Selected== true)
                {
                    if(i>0)
                    {
                        str = Language.Items[i].Text;
                    }
                    else
                    {
                        str = str + " ," + Language.Items[i].Text;
                    }
                }
            }
            Langcheckbox.Text = str;

        }
    }
}
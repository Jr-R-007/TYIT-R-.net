<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="Admission.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="FormView1" runat="server">
        <div>
            <asp:Panel ID="Panel1" runat="server">

                <table style="width: 100%;">




                    <tr>
                        <td>Photo</td>
                        <td>
                            <img src="Image/a.jpg" / width="50px" height="50px" ></td>


                    </tr>
                    <tr>
                        <td>Name</td>
                        <td>
                            <asp:TextBox ID="Textb1" runat="server"></asp:TextBox></td>

                    </tr>
                    <tr>
                        <td>Roll No</td>
                        <td>
                            <asp:TextBox ID="Textb2" runat="server"></asp:TextBox></td>


                    </tr>
                    <tr>
                        <td>Gender</td>
                        <td>
                            <asp:RadioButtonList ID="RadioButtonList1" runat="server" RepeatDirection="Horizontal">
                                <asp:ListItem Value="M">Male</asp:ListItem>
                                <asp:ListItem Value="F">Female</asp:ListItem>
                            </asp:RadioButtonList></td>


                    </tr>
                    <tr>
                        <td>State</td>
                        <td>
                            <asp:DropDownList ID="DDSTATE" runat="server" AutoPostBack="True" OnSelectedIndexChanged="DDSTATE_SelectedIndexChanged">
                                <asp:ListItem>Select State</asp:ListItem>
                                <asp:ListItem>Maharashtra</asp:ListItem>
                                <asp:ListItem>Tamilnadu</asp:ListItem>
                                <asp:ListItem>Kashmir</asp:ListItem>
                            </asp:DropDownList></td>


                    </tr>





                    <tr>
                        <td>City</td>
                        <td>
                            <asp:DropDownList ID="DDCITY" runat="server" AutoPostBack="True">
                                <asp:ListItem>Select City</asp:ListItem>
                                <asp:ListItem>Kalyan</asp:ListItem>
                                <asp:ListItem>Chennai</asp:ListItem>
                                <asp:ListItem>Shrinagar</asp:ListItem>
                            </asp:DropDownList>
                        </td>
                    </tr>

                    <tr>
                        <td>Language known</td>
                        <td>
                            <asp:CheckBoxList ID="Language" runat="server" RepeatDirection="Horizontal">
                                <asp:ListItem>C</asp:ListItem>
                                <asp:ListItem>C++</asp:ListItem>
                                <asp:ListItem>JAVA</asp:ListItem>
                                <asp:ListItem>PYTHON</asp:ListItem>
                            </asp:CheckBoxList>
                        
                    
                            <asp:Button ID="Langcheckbox" runat="server" Text="Button" OnClick="Langcheckbox_Click" />
                        <asp:Label ID="Langlabel" runat="server" Text=""></asp:Label>
                            </td>
                    </tr>


                </table>


            </asp:Panel>
        </div>
    </form>
</body>
</html>


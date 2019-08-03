import java.lang.*;
import java.io.*;
import java.util.*;
import java.util.TimerTask;
import java.util.Timer;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
class Khelo implements keyListener
{
int rad=50;
int xball=800;
int yball=400;
JFrame f;
JPanel p;
JLabel l1,l2,l3;
Thread th;
ImageIcon icon,icon1,icon3;
Khelo()
{
 f=new JFrame("Khelo");
Dimension d=Toolkit.getDefaultToolkit().getScreenSize();
		sw=(int)(d.getWidth());
		int sh=(int)(d.getHeight());
		setSize(sw,sh);
f.setVisible(true);
 p=new JPanel();
 icon=new ImageIcon("mario.jpg");
JLabel l1=new JLabel(icon);
l1.setBounds(0,0,1300,800);
 icon1=new ImageIcon("running1.jpg");
l2=new JLabel(icon1);
l2.setBounds(80,500,159,180);
l1.add(l2);
icon3=new ImageIcon("ball.jpg");
l3=new JLabel(icon3);
l1.add(l3);
l3.setBounds(x,y,200,100);
p.add(l1);
f.setUndecorated(true);
f.addKeyListener(this);
Timer t=new Timer(5000,new MyListener());
f.add(p);
}
class MyListener implements ActionListener
{
public void actionPerformed(ActionEvent e)
{
x=x<sw?x+20:-162;
l3.setBounds(x,y,200,100);
}
int x=20,y=200;
public static void main(String a[])
{
Khelo k=new Khelo();
}
boolean b=false;
timer t;
public void keyPressed(ActionEvent e1)
{
int kc=e1.getKeyCode();
if(kc==KeyEvent.VK_SPACE)
		{
t=new Timer(50,(ev)->{
if(y>100&&!b){
				y=y-5;
				b=false;
			}else if(y<300){
				y=y+5;
				b=true;
			}else if(y==300){
				b=false;
				t.stop();
			}
			l.setBounds(x,y,304,300);
		  });
		  t.start();
		}
	}
	public void keyReleased(KeyEvent e)
	{}
	public void keyTyped(KeyEvent e)
	{}
}
}
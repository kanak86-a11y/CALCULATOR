<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0" idbasedtr="true">
 <author>main.py</author>
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>463</width>
    <height>484</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">*{
	border: none;
	background-color: transparent;
	background: transparent;
	padding: 0;
	margin: 0;
	color: #fff;
}
centralwidget{
	background-color: rgba(255, 255, 255);
}
QPushButton{
	border-radius: 10px;
	background-color: rgba(125, 125, 125, 100);
	padding: 5px 10px;
}
QLabel{
	border-radius: 10px;
	background-color: rgba(125, 125, 125, 100);
	padding: 15px 10px;
    border: 2px solid;
}
QFrame{
	border-radius: 10px;
	background-color: rgba(125, 125, 125, 100);
	padding: 15px 10px;
    border: 2px solid;
}
#plus, #minus, #mul, #DIVIDE, #BACKSPACE, #EQUAL, #CLEAR, #PERCENTAGE{
    background-color: rgb(85, 85, 127);
    border-radius: 15px
}
    </string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="INPUTS">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>451</width>
      <height>381</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QPushButton" name="SEVEN">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>60</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>7</string>
     </property>
    </widget>
    <widget class="QPushButton" name="EIGHT">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>60</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>8</string>
     </property>
    </widget>
    <widget class="QPushButton" name="NINE">
     <property name="geometry">
      <rect>
       <x>280</x>
       <y>60</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>9</string>
     </property>
    </widget>
    <widget class="QPushButton" name="plus">
     <property name="geometry">
      <rect>
       <x>400</x>
       <y>60</y>
       <width>30</width>
       <height>30</height>
      </rect>
     </property>
     <property name="minimumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="maximumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>+</string>
     </property>
    </widget>
    <widget class="QPushButton" name="FOUR">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>120</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>4</string>
     </property>
    </widget>
    <widget class="QPushButton" name="FIVE">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>120</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>5</string>
     </property>
    </widget>
    <widget class="QPushButton" name="SIX">
     <property name="geometry">
      <rect>
       <x>280</x>
       <y>120</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>6</string>
     </property>
    </widget>
    <widget class="QPushButton" name="minus">
     <property name="geometry">
      <rect>
       <x>400</x>
       <y>120</y>
       <width>30</width>
       <height>30</height>
      </rect>
     </property>
     <property name="minimumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="maximumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>-</string>
     </property>
    </widget>
    <widget class="QPushButton" name="ONE">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>180</y>
       <width>61</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>1</string>
     </property>
    </widget>
    <widget class="QPushButton" name="TWO">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>180</y>
       <width>61</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>2</string>
     </property>
    </widget>
    <widget class="QPushButton" name="THREE">
     <property name="geometry">
      <rect>
       <x>280</x>
       <y>180</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>3</string>
     </property>
    </widget>
    <widget class="QPushButton" name="mul">
     <property name="geometry">
      <rect>
       <x>400</x>
       <y>180</y>
       <width>30</width>
       <height>30</height>
      </rect>
     </property>
     <property name="minimumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="maximumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>*</string>
     </property>
    </widget>
    <widget class="QPushButton" name="ZERO">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>240</y>
       <width>61</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>0</string>
     </property>
    </widget>
    <widget class="QPushButton" name="EQUAL">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>240</y>
       <width>61</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>=</string>
     </property>
    </widget>
    <widget class="QPushButton" name="DIVIDE">
     <property name="geometry">
      <rect>
       <x>280</x>
       <y>240</y>
       <width>61</width>
       <height>31</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>/</string>
     </property>
    </widget>
    <widget class="QPushButton" name="PERCENTAGE">
     <property name="geometry">
      <rect>
       <x>400</x>
       <y>240</y>
       <width>30</width>
       <height>30</height>
      </rect>
     </property>
     <property name="minimumSize">
      <size>
       <width>30</width>
       <height>30</height>
      </size>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>%</string>
     </property>
    </widget>
    <widget class="QPushButton" name="CLEAR">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>300</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>CE</string>
     </property>
    </widget>
    <widget class="QPushButton" name="BACKSPACE">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>300</y>
       <width>61</width>
       <height>28</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>C</string>
     </property>
    </widget>
   </widget>
   <widget class="QFrame" name="RESULT">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>451</width>
      <height>60</height>
     </rect>
    </property>
    <property name="maximumSize">
     <size>
      <width>16777215</width>
      <height>60</height>
     </size>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="result">
     <property name="geometry">
      <rect>
       <x>30</x>
       <y>20</y>
       <width>81</width>
       <height>21</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="text">
      <string>=0</string>
     </property>
    </widget>
   </widget>
  </widget>
 </widget>
 <layoutdefault spacing="7" margin="11"/>
 <resources>
  <include location="ico.qrc"/>
 </resources>
 <connections/>
 <designerdata>
  <property name="gridDeltaX">
   <number>10</number>
  </property>
  <property name="gridDeltaY">
   <number>10</number>
  </property>
  <property name="gridSnapX">
   <bool>true</bool>
  </property>
  <property name="gridSnapY">
   <bool>true</bool>
  </property>
  <property name="gridVisible">
   <bool>true</bool>
  </property>
 </designerdata>
</ui>

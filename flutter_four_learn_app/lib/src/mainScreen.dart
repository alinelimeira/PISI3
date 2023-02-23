// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'dart:html';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter_four_learn_app/src/MainMenuScreen.dart';
import 'package:flutter_four_learn_app/src/ProfileScreen.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int screenAtual = 0;
  late PageController pc;

  @override
  void initState() {
    super.initState();
    pc = PageController(initialPage: screenAtual);
  }

  setScreenAtual(screen) {
    setState(() {
      screenAtual = screen;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView(
        controller: pc,
        children: [MainMenuScreen(), ProfileScreen()],
        onPageChanged: setScreenAtual,
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: screenAtual,
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.house), label: 'Menu'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Perfil')
        ],
        onTap: (screen) {
          pc.animateToPage(screen,
              duration: Duration(milliseconds: 400), curve: Curves.ease);
        },
        backgroundColor: Colors.red,
      ),
    );
  }
}

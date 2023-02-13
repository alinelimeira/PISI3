import 'package:flutter_four_learn_app/src/LoginScreen.dart';
import 'package:flutter/material.dart';
import 'src/FirebaseAuth.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const FourLearnApp());
}

class FourLearnApp extends StatelessWidget {
  const FourLearnApp({Key? key}) : super(key: key);

  // This widget is the root of our application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: Colors.blueGrey,
        ),
        debugShowCheckedModeBanner: false,

        //Definindo rotas no APP
        initialRoute: '/firebaseAuth',
        routes: {
          '/': (context) => LoginScreen(),
          '/FirebaseAuth': (context) => const FirebaseAuth(),
        });
  }
}

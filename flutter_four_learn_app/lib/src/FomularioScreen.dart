import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:flutter_four_learn_app/util/dropdownField.dart';
import 'package:flutter_four_learn_app/util/textButtons.dart';

class FormularioScreen extends StatefulWidget {
  const FormularioScreen({super.key});

  @override
  State<FormularioScreen> createState() => _FormularioScreenState();
}

class _FormularioScreenState extends State<FormularioScreen> {
  final almoco = ['Reduzido', 'Padrão'];
  final educacaoPais = [
    'Graduado',
    'Bacharel',
    'Ensino médio completo',
    'Mestre',
    'Ensino médio incompleto',
    'Ensino superior incompleto'
  ];

  final preparationCourse = ['Completo', 'Incompleto'];

  final etnia = ['Branco', 'Não branco'];

  final nota = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

  String almocoValue = 'Reduzido';
  String educacaoPaisValue = 'Graduado';
  String preparationCourseValue = 'Completo';
  String etniaValue = 'Branco';
  String notaValue = '0';

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [Text('Formulário')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: SizedBox(
        height: size.height,
        width: size.width,
        child: Column(children: [
          Row(
            children: const [
              Padding(
                padding: EdgeInsets.only(left: 54.0, top: 8),
                child: Text('Almoço/Merenda'),
              ),
            ],
          ),
          DropdowField(value: almocoValue, valueList: almoco),
          Row(
            children: const [
              Padding(
                padding: EdgeInsets.only(left: 54.0, top: 16),
                child: Text('Nível de educação dos pais'),
              ),
            ],
          ),
          DropdowField(value: educacaoPaisValue, valueList: educacaoPais),
          Row(
            children: const [
              Padding(
                padding: EdgeInsets.only(left: 54.0, top: 16),
                child: Text('Curso de preparação'),
              ),
            ],
          ),
          DropdowField(
              value: preparationCourseValue, valueList: preparationCourse),
          Row(
            children: const [
              Padding(
                padding: EdgeInsets.only(left: 54.0, top: 16),
                child: Text('Etnia'),
              ),
            ],
          ),
          DropdowField(value: etniaValue, valueList: etnia),
          Row(
            children: const [
              Padding(
                padding: EdgeInsets.only(left: 54.0, top: 16),
                child: Text('Nota de linguagem'),
              ),
            ],
          ),
          DropdowField(value: notaValue, valueList: nota),
          Expanded(
            child: Align(
              alignment: Alignment.bottomCenter,
              child: Padding(
                padding: const EdgeInsets.only(bottom: 16.0),
                child: SizedBox(
                  height: 45,
                  child: SecondaryButton(title: 'SALVAR', onPressed: () {}),
                ),
              ),
            ),
          )
        ]),
      ),
    );
  }
}

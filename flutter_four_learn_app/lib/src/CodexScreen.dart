// ignore: file_names
import 'package:flutter/material.dart';
import 'package:charts_flutter/flutter.dart' as charts;

class CodexScreen extends StatelessWidget {
  final List<charts.Series<dynamic, String>> seriesList;

  const CodexScreen(this.seriesList, {super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [Text('Codex - Livro de Registros')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: charts.BarChart(
        seriesList,
        animate: false, // desabilita a animação
      ),
    );
  }

  static List<charts.Series<dynamic, String>> createSampleData() {
    final data = [
      PomosCiclos('psb', 3) //TODO ajuda para ajustar com o firebase
    ];

    return [
      charts.Series<PomosCiclos, String>(
        id: 'Ciclos',
        colorFn: (_, __) => charts.MaterialPalette.blue.shadeDefault,
        domainFn: (PomosCiclos ciclos, _) => ciclos.atividade,
        measureFn: (PomosCiclos ciclos, _) => ciclos.ciclos,
        data: data,
      ),
    ];
  }
}

class PomosCiclos {
  final String atividade;
  final int ciclos;

  PomosCiclos(this.atividade, this.ciclos);
}

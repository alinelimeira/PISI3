class Pomodoro {
  String? nome;
  int? tempoFoco;
  int? tempoDescanso;
  int? ciclos;
  int? ciclosEstudados;
  int? tempoEstudoMinutos;

  Pomodoro();

  Map<String, dynamic> toJson() => {
        'nome': nome,
        'tempoFoco': tempoFoco,
        'tempoDescanso': tempoDescanso,
        'ciclos': ciclos,
        'ciclosEstudados': ciclosEstudados,
        'tempoEstudoMinutos': tempoEstudoMinutos
      };

  Pomodoro.fromSnapshot(snapshot)
      : nome = snapshot.data()['nome'],
        tempoFoco = snapshot.data()['tempoFoco'],
        tempoDescanso = snapshot.data()['tempoDescanso'],
        ciclos = snapshot.data()['ciclos'],
        ciclosEstudados = snapshot.data()['ciclosEstudados'],
        tempoEstudoMinutos = snapshot.data()['tempoEstudoMinutos'];
}

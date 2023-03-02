// ignore_for_file: must_be_immutable

import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class DropdowField extends StatefulWidget {
  String value;
  final List<String> valueList;
  DropdowField({required this.value, required this.valueList, super.key});

  @override
  State<DropdowField> createState() => _DropdowFieldState();
}

class _DropdowFieldState extends State<DropdowField> {
  @override
  Widget build(BuildContext context) {
    return Container(
      width: 292,
      height: 60,
      decoration: BoxDecoration(
          color: Color(0xFF44CDEB), borderRadius: BorderRadius.circular(10)),
      child: DropdownButton<String>(
          isExpanded: true,
          value: widget.value,
          items: widget.valueList.map<DropdownMenuItem<String>>((String value) {
            return DropdownMenuItem<String>(value: value, child: Text(value));
          }).toList(),
          onChanged: (String? newValue) {
            setState(() {
              widget.value = newValue ?? '';
            });
          }),
    );
  }
}

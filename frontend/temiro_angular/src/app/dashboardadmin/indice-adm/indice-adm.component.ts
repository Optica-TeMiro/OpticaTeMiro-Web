import { Component, OnInit } from '@angular/core';
import { VisitasService } from '../../visitas.service'; // revisar que la ruta sea correcta

@Component({
  selector: 'app-indice-adm',
  templateUrl: './indice-adm.component.html',
  styleUrls: ['./indice-adm.component.css']
})
export class IndiceAdmComponent implements OnInit {
  visitas: number = 0;

  constructor(private visitasService: VisitasService) { }

  ngOnInit(): void {
    this.obtenerContadorVisitas();
  }

  obtenerContadorVisitas(): void {
    this.visitasService.obtenerContadorVisitas().subscribe((data: number) => {
      this.visitas = data;
    });
  }
}

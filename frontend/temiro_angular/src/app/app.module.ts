import { NgModule }            from '@angular/core';
import { BrowserModule }       from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';

import { AppRoutingModule }    from './app-routing.module';
import { AppComponent }        from './app.component';
import { ComunModule }         from './comun/comun.module';
import { DashboardModule }     from './dashboard/dashboard.module';
import { DashboardAdminModule } from './dashboardadmin/dashboardadmin.module';
import { HomeModule }          from './home/home.module';
import { RouterModule }        from '@angular/router';

@NgModule({
  declarations: [
    AppComponent
    // IndiceAdmComponent  // Este componente debe ser eliminado de aquí
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    ComunModule,
    DashboardModule,
    HomeModule,
    DashboardAdminModule,  // Esto permite el uso de IndiceAdmComponent sin declararlo aquí
    RouterModule
  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

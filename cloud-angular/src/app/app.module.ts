import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatExpansionModule} from '@angular/material/expansion';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { DatabaseReadComponent } from './database-read/database-read.component';
import { RestService } from "./REST-service/rest.service";
import { HttpModule  } from '@angular/http';


@NgModule({
  declarations: [
    AppComponent,
    DatabaseReadComponent
  ],
  imports: [
    MatExpansionModule,
    BrowserModule,
    BrowserAnimationsModule,
    HttpModule    
  ],
  providers: [RestService],
  bootstrap: [AppComponent]
})
export class AppModule { }

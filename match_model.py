from pathlib import Path
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///C:/webDev/pycharm/matchmaker/data/my_sqlite_db.db')#'sqlite:///my_sqlite_db.db')

Session = sessionmaker(bind=engine)
session = Session()


from datetime import datetime

from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Myco(Base):
    #32 items
    __tablename__ = 'mushrooms'

    id = Column(Integer(), primary_key=True)
    family = Column(Text())
    latin_names = Column(Text())
    english_names = Column(Text())
    notes = Column(Text())
    chemical_reactions = Column(Text())
    cap = Column(Text())
    nest = Column(Text())
    fruiting_body = Column(Text())
    upper_surface = Column(Text())
    flesh = Column(Text())
    outer_surface = Column(Text())
    habitat = Column(Text())
    gills = Column(Text())
    inner_layer = Column(Text())
    inner_surface = Column(Text())
    microscopic = Column(Text())
    underside = Column(Text())
    pores = Column(Text())
    stem = Column(Text())
    spore_mass = Column(Text())
    teeth = Column(Text())
    interior = Column(Text())
    eggs = Column(Text())
    name_origin = Column(Text())
    veil = Column(Text())
    odor = Column(Text())
    edibility = Column(Text())
    similar = Column(Text())
    taste = Column(Text())
    sources = Column(Text())
    spore_deposit = Column(Text())


Base.metadata.create_all(engine)


def dict_to_sql(single_myco_dict, session):
    single_mushroom=Myco(
                    family = single_myco_dict.get( "FAMILY" , "BLANK"),
                    latin_names = single_myco_dict.get( "LATIN NAMES" , "BLANK"),
                    english_names = single_myco_dict.get( "ENGLISH NAMES" , "BLANK"),
                    notes = single_myco_dict.get( "NOTES" , "BLANK"),
                    chemical_reactions = single_myco_dict.get( "CHEMICAL REACTIONS" , "BLANK"),
                    cap = single_myco_dict.get( "CAP" , "BLANK"),
                    nest = single_myco_dict.get( "NEST" , "BLANK"),
                    fruiting_body = single_myco_dict.get( "FRUITING BODY" , "BLANK"),
                    upper_surface = single_myco_dict.get( "UPPER SURFACE" , "BLANK"),
                    flesh = single_myco_dict.get( "FLESH" , "BLANK"),
                    outer_surface = single_myco_dict.get( "OUTER SURFACE" , "BLANK"),
                    habitat = single_myco_dict.get( "HABITAT" , "BLANK"),
                    gills = single_myco_dict.get( "GILLS" , "BLANK"),
                    inner_layer = single_myco_dict.get( "INNER LAYER" , "BLANK"),
                    inner_surface = single_myco_dict.get( "INNER SURFACE" , "BLANK"),
                    microscopic = single_myco_dict.get( "MICROSCOPE" , "BLANK"),
                    underside = single_myco_dict.get( "UNDERSIDE" , "BLANK"),
                    pores = single_myco_dict.get( "PORES" , "BLANK"),
                    stem = single_myco_dict.get( "STEM" , "BLANK"),
                    spore_mass = single_myco_dict.get( "SPORE MASS" , "BLANK"),
                    teeth = single_myco_dict.get( "TEETH" , "BLANK"),
                    interior = single_myco_dict.get( "INTERIOR" , "BLANK"),
                    eggs = single_myco_dict.get( "EGGS" , "BLANK"),
                    name_origin = single_myco_dict.get( "NAME ORIGIN" , "BLANK"),
                    veil = single_myco_dict.get( "VEIL" , "BLANK"),
                    odor = single_myco_dict.get( "ODOR" , "BLANK"),
                    edibility = single_myco_dict.get( "EDIBILITY" , "BLANK"),
                    similar = single_myco_dict.get( "SIMILAR" , "BLANK"),
                    taste = single_myco_dict.get( "TASTE" , "BLANK"),
                    sources = single_myco_dict.get( "SOURCES" , "BLANK"),
                    spore_deposit = single_myco_dict.get( "SPORE DEPOSIT" , "BLANK"),
    )

    session.add(single_mushroom)
    session.commit()



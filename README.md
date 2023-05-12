does-robot is a framework for making robots

by mark + jeff rosenberg

#### Requirements

A bash terminal

#### Installation

- `git clone git@github.com:doeswork/does-robot.git`
- `cd does-robot`
- `bin/setup`

#### Features

##### Priors

Get the prior `n` number of versions of a given file back in your repo

e.g.

`prior 3 parts/arm.stl`

would produce the following files in your robot repo

`current_arm.stl`
`prior_1_arm.stl`
`prior_2_arm.stl`
`prior_3_arm.stl`

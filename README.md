does-robot is a framework for making robots

by mark + jeff rosenberg

### Requirements

A bash terminal

### Installation

- `git clone git@github.com:doeswork/does-robot.git`
- `cd does-robot`
- `bin/setup`
  - if you move where your `does-robot` folder lives you'll have to `bin/setup` again

### Features

#### Previous

Get the previous `n` number of versions of a given file back in your repo

e.g.

```previous parts/arm.stl 3```

would produce the following files:

`current_arm.stl`
`previous_1_arm.stl`
`previous_2_arm.stl`
`previous_3_arm.stl`

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,bdd7d31bcb923de92d24ebfc2d5c90ba9da2328d@95.217.192.173:6090,218078f9caa4253dc5228995f86e8d7ff65d0e04@54.39.107.110:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.196:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,cc091c4d385e449a718fb252de800a9caf01913f@95.217.225.212:11656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

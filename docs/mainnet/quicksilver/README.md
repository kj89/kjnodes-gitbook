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
peers="51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.12:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,96bd0e87a5e5b88e8ce637aa3c7aa4f4803b1d03@51.195.234.240:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,4aa6607f87ad0b458526d3405731e71553cf275c@219.100.163.35:26656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,e1a24aaba30a8ff21e52fed92b96b36156b52e80@51.161.208.88:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ae3700d3296524014ab3444767df682b46f0cb9e@51.195.234.250:26656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,08ab5be08f12754381c0fd088bb36d9d294f54c6@65.109.21.74:26656,33720513faaa039977481782e33ffcb8ef67c4b7@95.217.114.220:11656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

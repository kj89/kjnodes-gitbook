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

**live-peers** (29)
```bash
peers="6053a39e67c6bae83430e354f53d99e160e4964b@65.109.28.177:28656,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,d36921a835076f6d87889793eb05a83099617221@202.61.240.122:26666,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,5ff3e4a15999abea4ecff260bfeaa30fa7390977@142.132.253.112:15656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,9284eae41fd79b5f5862702ee00ba4ea55d49f44@5.181.190.161:27060,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,2309e82e7200ac8a81f1e1f57b3ee604a20af853@51.79.177.229:26667,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,bdbb005129890e3b656841415b3b728d1e4529e6@176.9.155.98:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,ae3700d3296524014ab3444767df682b46f0cb9e@51.195.234.250:26656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

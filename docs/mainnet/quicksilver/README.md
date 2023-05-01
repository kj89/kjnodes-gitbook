# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

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
* grpc: quicksilver.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="fb1e7a989ff78f0bdd7828dc3ade95dcd67cd5d0@65.109.116.151:15656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,841efbdd6cd5c7191b5ec849499dfd9d1ea6a931@23.88.69.22:28566,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,2309e82e7200ac8a81f1e1f57b3ee604a20af853@51.79.177.229:26667,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,a9e0f3c8e84c575492a2ff454abdad3b4762e712@193.34.212.166:25656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,4aa6607f87ad0b458526d3405731e71553cf275c@219.100.163.35:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,0521c200a3dc430927978fb2c66293b8481fc3ae@198.244.203.181:26656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,ae44851a5d63d70382c1621bc7727db2a40d10d0@88.99.164.158:21026"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

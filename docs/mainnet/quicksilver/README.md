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
peers="5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,c2a44958de52a8656eba9eedaf88205f27686ffd@46.4.23.42:11656,43b97f492bf47b455b7b275c396b1840f4eb336d@142.132.139.101:26656,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,ce3837aa07eb0967c024d4c592f7c2730754bdd8@157.90.179.182:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,5fa47201aa5208c30982b6f9d8ca44222d256fc5@51.91.70.90:48656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@142.132.253.112:15656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

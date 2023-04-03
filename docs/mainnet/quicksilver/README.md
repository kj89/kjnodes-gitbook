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
peers="ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,ec076ff33f2986d064b78602e2ccd2c925bf761e@161.97.82.203:26256,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,1b569bf57da79df4f85d207a161a97626988af76@65.109.92.241:20026,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d36921a835076f6d87889793eb05a83099617221@202.61.240.122:26666,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,0de3ea135f09f6fcbe8ab75208ef9ca2e4b13d89@80.64.208.149:26656,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,03b3e3093b6cd33fba9f00cea6c2a560f89c61d6@195.14.6.2:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,d11e03ee30496ef827383d5dcbbc55e7b3171189@35.240.184.52:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,0dfdec8a3bba26ad4258d3fd67a8468c10c3109c@195.114.30.92:11656,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@34.107.62.213:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

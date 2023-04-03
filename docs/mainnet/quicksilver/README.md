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
peers="bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,71d1e3336f41475c3dfc247aa77a8842a24c369a@144.91.80.32:11656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,21d8608d89e51b9ff806846538a45aed2aa25063@95.214.53.105:44656,11a72b38d740e50f54c05d6084030bc9ed29ce7f@212.23.222.126:30573,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,679f56feb7f4f91d46a92d0eb474d1dc43466d18@213.239.215.59:29986,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,9f0770c748d9323223722faacd30262218287b40@65.108.238.102:11156,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.12:26656,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,d11e03ee30496ef827383d5dcbbc55e7b3171189@35.240.184.52:26656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,663134c4999f4f9fc59879eaaebbb332e91e2160@45.34.1.114:33656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```

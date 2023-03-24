# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (38)
```bash
peers="f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,3693ea5a8a9c0590440a7d6c9a98a022ce3b2455@65.109.92.79:20656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,1a18bdd0c259d604cda023a5e03eba2a25f5c045@94.19.249.187:27656,6a390c192797c62837030ad9058d4be672db4a0e@154.12.245.38:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,d7c350f9b16111f04a5fe391ec8ccbed5faee56e@86.48.1.218:26656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,7e851a5714dff9276bd5a73b4d5c64bab6b1faca@135.181.16.252:33656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,236ef342a0063ddb677ebac5f4e5ff37d87cb929@65.108.3.81:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,a7cad1d8aa2b5fa2070c826307cdaf09bbf114f6@212.227.233.231:36656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,7e13f5a41b15993f6ec2b3d5b8bd79c6a8c45c59@65.108.154.229:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

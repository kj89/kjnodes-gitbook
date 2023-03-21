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

**live-peers** (35)
```bash
peers="0eb2dba8e99f29941edaf58974f469635479562f@154.12.245.39:28656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,4bb3bb98ca32b5a0f82d445e60065601bb93a38c@86.111.48.163:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,2e5ab5fc9ebf84aa2d2e5c707461e3ad0d59da80@146.19.24.242:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,7c2af4cada7df34da4161feaa4c90dd278ca75db@65.108.108.52:21656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,f7c1a998b8ef7cae7e38b0eff64d96206924e957@45.84.138.167:26656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,695f9e8dad50fa524ed96c4d5df7afe12963995f@65.108.124.219:38656,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,8a01be4f582013d6446672663a84ff18901f82c3@38.242.223.2:26656,6c6e8b47a8edbe6a858f89c890c12ae9689900e5@95.216.221.194:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,22668060b7bb1ec790015422d9287bae3444bade@185.107.237.212:38656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

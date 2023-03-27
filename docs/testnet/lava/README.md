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

**live-peers** (36)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6a390c192797c62837030ad9058d4be672db4a0e@154.12.245.38:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,c84dc5a9719a92be66e89e0379867b9fb79639b2@157.55.181.152:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,4e0a2772bb3672e54c2ea655c30abdac62191f14@45.84.138.66:18656,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,8f79bf6093fd728359f529a4a5214c0364749230@65.21.205.248:11656,5524484358f731e0863ec473b0cb7a4531956325@178.18.246.170:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,dced9544a6a8529980dee3ef5b40a251ef06b763@157.97.108.38:20656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,e3c92ba5f1ebd8bec0ab9431eb183ed9864eca87@65.108.231.238:46656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,dcb0ac5dbbd9869f3fd556c9e5cf41c23e22121f@20.219.189.105:26656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,5f04e56cabc20ab2e94b03022f024a310dfdf840@85.10.198.169:11656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

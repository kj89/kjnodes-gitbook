# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/composable.png" alt=""><figcaption></figcaption></figure>

The complete infrastructure for cross-chain smart  contracts, applications, and modular functionality.

**Chain ID**: banksy-testnet-2 | **Latest Version Tag**: v2.3.3-testnet2fork | **Wasm**: OFF

[Website](https://www.composable.finance) | [Discord](https://discord.gg/composable) | [Twitter](https://twitter.com/ComposableFin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/composable-testnet](https://explorer.kjnodes.com/composable-testnet)

## Public endpoints

* api: [https://composable-testnet.api.kjnodes.com](https://composable-testnet.api.kjnodes.com)
* rpc: [https://composable-testnet.rpc.kjnodes.com](https://composable-testnet.rpc.kjnodes.com)
* grpc: composable-testnet.grpc.kjnodes.com:15990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@composable-testnet.rpc.kjnodes.com:15956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@composable-testnet.rpc.kjnodes.com:15959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/composable-testnet/addrbook.json > $HOME/.banksy/config/addrbook.json
```

**live-peers** (30)
```bash
peers="0cc331c2ae0b907fef8911ec9f76e28b363af15e@176.9.2.2:40656,a1fc0664aa60511a96f665de740beb8824e2e1f0@65.109.80.176:30656,e31d7a9d6c6f9b372fd26512ef2d11e4c31ed226@65.21.134.202:26616,a7fdc284303bc4a8e62782e2e8f81008ea45a2b2@5.161.104.182:26656,96f7134bb4d8f2dce88d5509e5295fdc7d433c66@95.216.7.169:56656,0b9d9c0d6f1ff6d63f6e164895351e184c046ca2@134.209.38.116:26656,e6aa2a81f4b48b99d4d3f2ecd7739596af56d34d@148.113.143.196:26656,fe82bb3e15e4cee715f47a9ccb925134b9131669@46.4.213.193:26656,2ca32b1aba0208008738ddefe44d5239bef2e894@95.217.144.107:22256,156d57dfe94634eaba1c30f9ec2ce5ccee8410e1@65.21.88.12:2000,872c8a78a17a24d6f44e1126c46ef52069c7bb18@65.109.80.150:2630,7fc16efbb3e56d81245a0828198d580b3f246f58@51.91.30.173:3000,8859e665f2eca25da78aaf4d2e541407885b08d8@5.78.72.11:26656,7521d65a4102259fa26816383fea2f8f21a3b1ea@65.109.116.21:11154,d9b5a5910c1cf6b52f79aae4cf97dd83086dfc25@65.108.229.93:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:26976,48246fed451b0d553239a1a0ba13d84977584be9@142.132.207.187:26666,b13a2ff87cf8ea23773f2f3d8ad5b96ae7eb0b0b@65.108.206.74:36656,eba3bc4613f3dac61201374ce09bee1fad00dc54@51.91.219.141:44003,a9f62bf2505ba9dee4503ad0c383ad31a787d75a@212.23.222.6:11156,c4c51318e4d9a863c019fb277e5ed6748590e5c6@66.45.233.110:26656,a1bbf456dffa2d23bb9d524382f2f3c8e28a470e@34.142.142.40:26656,068fbf2425c5f024986444f1388fc1cabff3d733@46.4.5.45:22256,d850d1525f38622c2e8ea97a2ff91c63f8c8669c@193.26.159.34:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15956,5070c358e90f8005b2049ff2e6d8e95adeb9bdd3@144.76.182.73:40656,7bff2e43489a7acd09a38ab47c1f25ec24e24947@51.68.166.235:26656,6d26d7437e9075fbe01012a462aa522aef0504bf@136.243.148.154:40656,367de894f877be9a9592f9d506c3082798b603e9@148.251.82.189:40656,20f2608c9bc262df91d96027e1d5054ddee9c86c@142.132.209.236:22256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.banksy/config/config.toml
```

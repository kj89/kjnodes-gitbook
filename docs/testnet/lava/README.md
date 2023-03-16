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

**live-peers** (40)
```bash
peers="80922095c0766aabdaf9e93e9c38c45321347ac0@85.239.237.85:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,80ab0928eca4cb414a78103a8ca011e6734e7064@194.163.162.12:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,10746de4c5d27b0f443507f13d1479188876791e@65.108.9.164:48656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,abef1d647b77b701d81ae15e093bf00d29cc56e1@46.4.50.247:13656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,112fba64a7e5e27b0cf8f02c634334c957891abf@75.119.146.244:28656,f762b211ee317e8cae9f8ca8cd17a1de1e87f0df@116.202.8.211:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,df06418afe0c3d6ebbe8cd233dc9bed02b87cc62@65.108.107.241:26656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,60be50fae1525143ea9226eff17830c4a474af6c@154.53.39.80:26656,194ad0ab2f1003e123085300b0ca16d57e223be8@94.190.90.38:7060,67dae0d05a857065afd0286d134cbed1c8e9de40@38.242.231.22:29656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,8ffa4dbef4c0b2a1dc1172760914e2df1468fb22@178.63.8.245:60756,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,2c2410774b668e4ff208cc37a4b229f27a494cb5@81.196.253.241:47656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,fa908ede438730a87c02e113a95aac206398706d@207.180.207.68:26656,8bebe6d7420b7e7eed4f3d97fe96ee44c258de9f@185.216.203.44:26656,7546454d0cd3075d6cd73b0384ed1d9413ca477c@93.100.232.183:38656,31550f0ec97d7148b2dae0de2a02240f88d1cfcf@85.114.134.219:12656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,14110234a060fc0d9568fb43a32c8b6b0f0f8cc2@65.108.240.151:26656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,afc25b4b9f88c5af73c221475c47ba4c1cce4ae7@34.27.247.0:26656,ce67e9671e7212695a0a7ba27fb0c723ea6ccff0@35.225.146.131:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,b4c682261a1d6114e00a32bef17bd43398c7496c@164.92.241.245:26656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,2031e65ee8a13e57d922a14d28d67be0ada21a95@3.252.208.167:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,186bd321a742e88cce82425af3964b940ac59e07@207.180.218.54:26656,84d5e567c179738963bb500b3756c77708dd6039@65.109.6.62:26656,f9f49cc8ffbdee85fb8a9551f644f5554a610ebe@91.107.137.90:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,22bd49cb251e649816d2cb6f24897dd2b4602dc4@149.102.157.34:26656,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,642d88c7f4dc9f539721e2fe1e1dc949af5ca64a@82.115.26.58:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,810bdfb3e88f4872995f9a05b6298c1bf3d20fe0@65.108.105.48:19956,cd18e526efa1021864c07f8b4494f9413ea04fb2@35.184.2.75:26656,7e93260df1c1b6322b8ef229556264430cd83193@207.180.229.79:26656,7022dbc496c5cc645df6a44f792b40aa150844a3@62.141.44.209:38656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,8613c086d3d0e0e3cfafe5a8e75c398dfb0e603c@167.86.71.155:28656,d9abc551547563e9a45160adc070b8bb42fc7d62@75.119.134.69:29656,d51cd75c1356a209571765827540873ee588f861@104.131.161.235:26656,632bfd3276ab33ed74cbb048a1de28183b927e9c@80.85.141.179:26656,2702c1b9ce3a2b33ad7ce4e6fbb165b4ba55feae@109.111.160.171:27656,48550e0de9e2ba9754734e9c677f965440c6bfaf@183.182.125.15:26656,f31c4dc121f37db1e0e24b49584bbbe4bbbba6c4@162.55.39.16:36656,4877ad7cf06e277399808d8130a8f25a780a52b0@207.148.122.124:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

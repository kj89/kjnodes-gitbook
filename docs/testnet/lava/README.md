# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.9.8 | **Wasm**: OFF

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

**live-peers** (30)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,ed295c3ece2ded17ea4007a680154db83abeca13@95.217.114.220:13656,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,903cdd03466f29f5225c4ba51df788750fa87065@65.109.129.253:26656,07277038190e9eb8855a49b1a13d742d18d9bea5@65.108.41.172:26656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,95c59c9236f2e1c1c9ee35c6a9cd1b9f2fdc362e@213.239.215.115:29956,1db3eae2768388f2b613e0dae62763db1aba7994@43.204.255.101:15656,653bb90f4e8a1db9dbbeadd7bd5ae7fd1e1bb7e6@65.108.101.4:23356,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,a54db7f2f509b73a9376037343a063049a11fc56@65.109.111.159:38656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

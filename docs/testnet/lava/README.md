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

**live-peers** (28)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,57474bd0977b3ed65cf23086b6d1d92bf00d50d0@207.180.236.122:31656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,5600a9eed5fdf290229aacb21344398be81dd9c9@65.109.237.237:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,c55e0f1c1916bfa35127ca194263fe65c75c2995@38.242.251.1:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@195.201.76.69:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6570e2cab2a58255b7fad2f88e677eed55da1018@192.3.80.242:26656,f642b376722d6ce104ffd4c204e78ffe811e16c3@5.75.230.221:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,308d0792a496579601156d15cc02112150d89162@45.140.147.117:27656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

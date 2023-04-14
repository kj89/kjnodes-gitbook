# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.8.1 | **Wasm**: OFF

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

**live-peers** (21)
```bash
peers="0a528da95ca8025ef4043b6e73f1e789f4102940@176.103.222.22:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,9872ab6a76199fcbeca1f7f791755e726aa97686@116.202.165.116:11656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,ef6e9620807e7e4614fd8e02722f8075ec277544@199.175.98.122:26656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,3693ea5a8a9c0590440a7d6c9a98a022ce3b2455@65.109.92.79:20656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

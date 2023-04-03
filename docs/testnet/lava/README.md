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

**live-peers** (29)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,51aeaa2c757989f720c904023c2dbedfc720f75e@23.88.5.169:27656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,4f9120f706512162fbe4f39aac78b9924efbec58@65.109.92.235:11036,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,5ed48f1abdd16d62f2179af31af3789ac5a42ecc@34.142.220.216:37656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@195.201.76.69:36656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,91c02af6333972f222570a73f51feccda8a3ccf1@65.109.93.58:26656,105a3164a545ee2b91d0765cfec348a4f5af2424@194.233.71.228:26656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,e621280c25aa656a0abe3e79cac4e02e8b2b520a@46.4.53.207:36656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,b710c54a27dfa2ee3e9028a38060e3733bd2794a@130.185.119.103:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

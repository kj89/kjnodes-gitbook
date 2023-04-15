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

**live-peers** (24)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,3177033dfc8a88c0b1a4500e2812c74f41e9a32b@94.130.236.21:26656,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,4373d820675ffcad758892bbd8e442d545cb1f4b@86.111.48.155:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,5a542163bcfbfe8119745c0407cd74e2b09729f9@92.55.63.130:31656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

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
peers="13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,4ad3f3731073a016fa0c99118b2a5a2d313928f5@207.180.233.148:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,125935f63c123b6891b014ffc071fbf781270771@23.88.74.54:11656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,897d44b1cb6633539cf51261f6629a9d5664eb9b@159.69.72.247:11656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,5b337f7ba27e2fdd27918be18af93f8728034267@65.108.41.168:26656,a5637262d92b9c503d6abbb181d58a2314f67e1d@84.46.243.129:26656,c32d101819cedf78ea986e6d832e2306fb6d0649@185.248.24.224:16656,ca37f777c8b6bf5418eb86ca6b2762470b643ea8@95.216.42.95:26656,51f74e630050571b20f490bd47ad155a7f219cbb@173.249.54.227:29656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,1829486da26d7b88fb2a921798bb70f9218fc052@14.191.217.156:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

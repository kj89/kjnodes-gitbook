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

**live-peers** (18)
```bash
peers="25da069c4dca143029ddae47bf2b7de69c2a8678@65.108.9.164:21156,92f8e4caaadb2f00c95e03068933f2045a93e910@65.109.65.163:21156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,e5aff8690b3fc34f81c1792d56ba5d182cce68e9@65.109.116.204:21156,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,07277038190e9eb8855a49b1a13d742d18d9bea5@65.108.41.172:26656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,60be50fae1525143ea9226eff17830c4a474af6c@154.53.39.80:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

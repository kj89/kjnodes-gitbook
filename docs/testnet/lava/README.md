# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.10.1 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:14490

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:14456
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:14459
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (10)
```bash
peers="147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,2a588e5ddcfd8c9095cc6f34b5b6966e31020cfd@65.21.123.172:11656,d8e81881ced029758f9623179a3c1ecf72aece2e@195.74.86.49:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,3456c9ba0df46cbb526717d73fa51ff0ed9a53a1@95.216.14.58:60756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

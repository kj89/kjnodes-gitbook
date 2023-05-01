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
peers="ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,7aa9d96f0a3f162385b743ef92a2c6e03a4a1d84@65.108.48.77:20656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,4dbe5ebf1505f472d852cf7732343ceb899d51db@95.217.57.232:60656,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,34a0258d5f63b9033aeb71226a6fb1e4c4138682@52.14.52.73:26656,b294ab07592bb93a85b099fb684dd96a98e12ba9@178.63.102.172:23356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

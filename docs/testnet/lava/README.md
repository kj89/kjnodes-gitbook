# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.11.2 | **Wasm**: OFF

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
peers="5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,13a9209a4d08803a3becac57de8eb02dd51f8f41@65.109.23.114:19956,2a588e5ddcfd8c9095cc6f34b5b6966e31020cfd@65.21.123.172:11656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,bee277da0e5b235e0a7e38ea90d8547924370dbe@65.108.227.112:13656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

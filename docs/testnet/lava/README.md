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
peers="4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,e268a2ce255d51a93e6ec89ee73c233bbaec70f4@49.12.185.46:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,9a151159039fd8abce61ddb21e5342605787792b@5.75.228.39:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

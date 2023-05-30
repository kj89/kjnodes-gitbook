# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

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
peers="5c107bb2b72c930a5ab3406a1f7c7345b7229b49@148.251.11.99:11656,1fd86f6ba06ef4b189276f97f70fea04161019db@144.76.176.154:11656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,4732ed188fbe7603f81d9f4c825397277bb72217@5.75.235.195:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

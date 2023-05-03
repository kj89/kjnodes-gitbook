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
peers="6171a52cf0ffc1706409d2dcec56c1db81c86aae@176.103.222.17:26656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,342dbbf200eb906eed6901cb5edf6d341b4ebc9b@170.64.140.230:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,5d24eb95fa5974af7bb03e370382537251ab6328@95.217.158.66:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,370ae92bd28701e0c1d8dc912ccf0d40fe0db3d5@157.90.245.166:26656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

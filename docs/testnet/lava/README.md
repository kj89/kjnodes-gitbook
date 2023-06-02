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

**live-peers** (11)
```bash
peers="695f9e8dad50fa524ed96c4d5df7afe12963995f@65.108.124.219:38656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,21eb46c44f46820e42cfe4afbe2f1104eef95cfc@135.181.221.186:30656,b294ab07592bb93a85b099fb684dd96a98e12ba9@178.63.102.172:23356,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d796c20b5bdb8f1633c2a13afbf12314a77b668c@91.107.148.113:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,257856431ef33f9fbfe6c119fdf3820035891d0c@38.242.197.140:26656,5d24eb95fa5974af7bb03e370382537251ab6328@95.217.158.66:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

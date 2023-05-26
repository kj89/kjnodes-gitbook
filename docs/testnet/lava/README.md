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
peers="4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,147cf727f179eccbd29de3ebf5899c1f4a93f6de@46.38.235.53:26656,e1383b216c42acc842193c5ac7321ce6c0d73db0@78.47.37.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,21eb46c44f46820e42cfe4afbe2f1104eef95cfc@135.181.221.186:30656,bd1e1f8df77e7b61200c490c9fabe6bbc4412d4e@91.223.3.144:26856,ef38861694f07881410c1b1c5852c72050831d68@95.214.55.74:26656,ef1b3374ca00c338de50d51fc41ca317488156eb@207.244.245.41:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

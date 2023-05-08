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
peers="a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,8b154033143fdedf4835dfc7b030c7d781bfd54e@195.201.219.227:26656,2c419186cd96b59fe8b3307c54c27d6805414aba@65.108.8.28:60756,37add870e1f40b6b00a55b71d20590b2128fdd3d@88.99.33.248:26656,ba78f0ac713d5e7a0274ef593674dae337aabbee@176.103.222.18:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14456,e1c09e10296de98d5637e0f948ada9d477ad4d75@31.42.191.74:36656,0e9062ed560ce78eba346f1d73ae3ca9eeea5985@142.132.248.253:24656,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,c40a7bc3c7aee0428273c0bfa75fcb14bf0f44c4@65.109.90.171:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```

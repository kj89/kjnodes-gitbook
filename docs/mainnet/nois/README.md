# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois](https://explorer.kjnodes.com/nois)

## Public endpoints

* api: [https://nois.api.kjnodes.com](https://nois.api.kjnodes.com)
* rpc: [https://nois.rpc.kjnodes.com](https://nois.rpc.kjnodes.com)
* grpc: nois.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:51656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (18)
```bash
peers="d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,871066c94ef32f061f5f3db4d7a6d94b38d73c0f@65.109.92.240:40136,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,ed0cce5194ebefdf2f4d9301efc9a12101c35aa2@57.128.163.232:26656,85a26b34868cec6f9688eae38c4d2effe7ca8079@195.154.94.166:28709,3c5926d0b4b8750f16f6495063e6d762b2556d1e@65.21.122.47:27656,78c9915ae359907266e0eb713b911bdae21b4876@136.243.103.32:26656,8cce0e919b1a7c42086a712748c8e84d7d7cd9ac@135.181.155.14:26656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,e541e3a182bcb8d8da8cea17716d12f0b730a0a6@144.76.40.53:17356,c695f41458b08fe87729beffa513f1c38d20d1db@193.70.33.64:17356,563162895c3152ba7c46b115cd79f5d75017e9dc@65.108.138.80:17356,22ec344512fc679e16eb358284e0d1eaa4291194@142.132.253.112:36656,ae02b0a36568a1f2be71bd98840aae333d1e3147@51.159.195.168:46656,40692288807db7ac022e24e9247cd60e7fc995c7@81.0.248.57:17356,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```

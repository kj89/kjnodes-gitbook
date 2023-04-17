# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,8166c8aed5cd887e02b47e269062b4280e9f6437@89.163.157.60:40656,020abb71537ac87559814e1cb85cbd837046e836@23.88.5.169:23656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,8abfa09fdbea667157d96f79c815fd9b3186b6ae@65.109.92.240:2026,06c0fe8a5df43f71e88eaa3c07891338026ade9b@193.34.217.164:26656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,5b9504d6ba486791cee27e7d7aea247459c044ad@65.109.89.35:26656,24a4ddf356553cdf544c977bcd424b2b4d5e99c6@135.181.26.181:40656,9d62097edd303eefe1ea7b4a51a76e50d09cdada@185.16.39.13:26656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,96178b0c330c17fca47d8ed590a4bbf98526ca01@5.75.234.93:26656,0e191c0d1fed5e6745bee750309a9730beacd667@178.239.197.171:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,7cf6dc70e9dfa82db373120de0d79dddc71bd74e@194.34.232.99:26656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,2ea2700b0082d8d5bc9ed2f13b36af47cc787ea7@80.254.8.54:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,70a02b29719f2a3f7347e03aac2681af6c634f33@158.220.100.181:40656,912d95a925bb827e1f6ac08810742d658fd2268e@185.218.126.186:27656,d65109b0e823b26069be5ec255f84608fa98a100@89.163.213.61:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

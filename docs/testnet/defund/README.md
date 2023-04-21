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

**live-peers** (27)
```bash
peers="0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,94d5df9524fc6eb12df19c814455de5f7a07c042@46.38.232.86:21656,70c35e37f399fe02d41823c97188a4e5911d5b17@38.242.217.231:26656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,d3f613337f8b4c52fc7363e70df93422327ea925@23.88.32.193:26656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,9afc6f16f21823d3850f5d18f66de786ea9ecea5@94.130.218.86:13656,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,73657fd476a5a21f74e2f9d61ddc24709035b9c2@65.108.209.237:40656,70a72a3fdec5195882e99abd023badce1548d9c9@155.133.22.134:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,2da5c563e31d3f3a0101f55ec6186d65465881d9@95.217.88.248:13656,1ff43841e4395dca585678be6a790df9a037f1cd@209.38.252.86:26656,789f5035190704fac04402363713179cb6c6ad00@109.195.139.31:26656,2fa0c6e23c2ca348c1664ee27c84f6b177623467@95.217.59.120:13656,126524e1a563d9e7082de4fea61aac69a724760f@188.34.182.100:40656,627c4432dbbcf879a3d5855d247bec70e91443ff@95.217.184.23:26656,c917ffe5d1ca980f75e11aa35f2135b735f9f1a6@143.42.183.90:26656,e0f6aea18a4b888e00ce66f7275985b289db726e@89.163.157.64:36666"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

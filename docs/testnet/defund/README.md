# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

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

**live-peers** (29)
```bash
peers="22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,a3ede88696b2b5f752129889b84b9292a168133a@142.132.152.46:21656,c9bd11543948f94d715839d39ae6bfa23deedf74@161.97.78.178:26656,c917ffe5d1ca980f75e11aa35f2135b735f9f1a6@143.42.183.90:26656,7dff00a6d6678dd1f29df92774bb15cda17fff28@185.92.149.140:26656,55d896d8da08838d0d7079b8953c74b7b9519ac1@164.68.127.158:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,8e039627e5fe9f829b20a71d93ba40e015d0a0d5@135.181.128.249:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,15d053c8b58877f598331da4b7851f6faf990fb2@65.109.89.35:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,c584a5f8c28c7548752fdfea6cf2942d5e10c82e@188.34.178.190:56656,6a5846b11911d2c6cf5602f98dafbe68b778ad63@65.109.89.43:40656,19ce67b3c44238b09bebd121ef7341b14a3ff0b9@209.145.62.91:30656,1f526dc91429dc7c98d5b0ceb49f84f64c11336e@65.108.243.55:40656,11312b65dd8010042f286e7173d2bcc7a35b2550@46.56.82.117:26656,e7f2e1abef350b013ae9bc488277cba45bd6b13a@65.109.106.211:40656,b8f0bee92d7b87ec4b9abf15888fefb6d2e07092@142.44.143.93:24656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

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

**live-peers** (25)
```bash
peers="cf28e64a237c7278223238325727cef0c2c8ca51@193.34.217.174:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,af9f3f65b3082007020697d035e7d5031e3be25b@212.23.222.89:26656,6ae6e82fe96e9386e40050958f2f3722cdad9826@178.205.12.0:26656,dc23977a6d03fe61a3ed3eb3eda775683219f958@178.64.25.243:26656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,115c9212457522139817a7703cb5ca97d1a48c4f@81.0.247.136:26656,d16c05133b6cf47791c2442fa2452f5abaa2a12e@144.126.138.81:30656,7d51a0519639c75d7a33f7ebe22319b1ef9eb9ad@185.209.230.89:26656,5d76132a47eea874b3b451182b48ae6289c2d2f3@194.146.13.253:26656,38087da52aa2cac5affd19eccb0e1401bc953c6b@65.109.90.171:33656,b654f4b9394fcb6a98ca5845c70bb4026aa34fda@209.145.62.91:30656,e409c0c3dc1307aebad1e112bf381c8ac8d146db@167.86.74.107:26656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,6f82e772ee8ae1895edc9743dbb269fb7c33f06a@144.91.89.158:30656,62f1b6e0958f7b5c6a81c90ed9bbee0ea87c86f4@88.210.6.152:26656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,ee0e944debde1a975ac77ee468d2f9723f25468a@144.126.138.107:30656,41605a6e5b6e22e349e67e8f9088ac93b958e104@45.94.58.246:40656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```

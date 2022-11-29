# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

Website: [https://uptick.network](https://uptick.network)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (30)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,0aee682fb3453170737149203e5c23d2e0c46058@142.132.253.112:15656,fb6dba36fcf9f62a817558c0bd10e114ac8c44cc@116.203.183.189:15656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,f94be046ec5f2b0b7096541cd157bd33f62c360d@95.216.68.96:15656,3cffe20d473b0bd4451d330da8b741b5d42dcb44@65.21.131.215:26666,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,e8704845eaa0f3d39fcdc9c4065f3beb344384db@142.132.152.46:27656,7a1f08486cd519270b3aeab7c6c4abf2cc07d22b@46.17.250.145:60856,2d892493335b4bb1582dabcaa1e832bcba041e79@95.217.4.62:26656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,f296bfda3c0c3f46059c89d3ee02f3f11d95d00b@162.55.234.70:55056,20aaf646f9c766a8b81d838554ba6e593122ed1f@46.4.122.236:36656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,8340a33a3794dfef56159f412012c16ce51d96dc@65.109.85.52:46656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,821cec653e1bdcd6e0ea7db62ddc65e7dae9fc5b@190.2.136.58:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,96a2fd192db329ff9df3f44569f0fe452ea9f19e@65.108.232.110:15656,40e340692ead998ad22d4c5907d4ca27ac1cdbc8@65.109.34.9:60856,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,0105e6bcc1d69031d27817110050319446101362@65.108.197.178:31656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,6b5375296e81501b0db0a34a7a04f39520400214@65.108.45.200:27565,962e467376dd18f68bbab10cda5a336a1a08aa4b@65.21.134.202:26666,b1f4cbece3a83ea55ba28a50281eaa3af9119cd4@65.21.129.95:21256,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,79888e0547bfb9937e4a6f4fbdca7ccbf46cbbde@155.133.23.88:26656,75aa14851ff12bd4825fe5679958dc278086e2b9@95.216.14.72:34656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
